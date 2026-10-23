"""Regression checks for the supplied hospital-data sources."""

from pathlib import Path
import sqlite3
import unittest

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_CSV = PROJECT_DIR / "data" / "raw" / "hospital_original.csv"
RAW_XLSX = PROJECT_DIR / "data" / "raw" / "hospital_original.xlsx"
SQLITE_DB = PROJECT_DIR / "data" / "hospital.db"


class HospitalDataIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.csv_data = pd.read_csv(RAW_CSV)

    def test_sources_have_the_same_records(self):
        excel_data = pd.read_excel(RAW_XLSX)
        with sqlite3.connect(SQLITE_DB) as connection:
            sql_data = pd.read_sql_query("SELECT * FROM hospital", connection)

        # SQLite represents an all-null column as Python None; CSV uses NaN.
        sql_data["Medication"] = pd.to_numeric(
            sql_data["Medication"], errors="coerce"
        )

        pd.testing.assert_frame_equal(self.csv_data, excel_data)
        pd.testing.assert_frame_equal(
            self.csv_data,
            sql_data,
            check_dtype=False,
        )

    def test_dates_and_length_of_stay_are_consistent(self):
        admission = pd.to_datetime(self.csv_data["Admission_Date"], dayfirst=True)
        discharge = pd.to_datetime(self.csv_data["Discharge_Date"], dayfirst=True)

        self.assertFalse((discharge < admission).any())
        pd.testing.assert_series_equal(
            (discharge - admission).dt.days,
            self.csv_data["Length_of_Stay"],
            check_names=False,
        )

    def test_patient_ids_are_unique(self):
        self.assertFalse(self.csv_data["Patient_ID"].duplicated().any())


if __name__ == "__main__":
    unittest.main()
