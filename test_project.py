from project import get_raw_data, get_requested_metals, move_data, get_sample_data
import pytest
expected_dict = {
        'sample 1': 'metal 1',
        'sample 2': 'metal 2',
        'sample 3': 'metal 3'
}

def main():
    test_get_raw_data()
    test_get_requested_metals()
    test_get_requested_metals_file_not_found()
    test_move_data()

def test_get_raw_data():
    with pytest.raises(FileNotFoundError):
        get_raw_data("raw data")

def test_get_requested_metals():
    print(get_requested_metals("test_excel_sheet.xlsx"))
    assert(get_requested_metals("test_excel_sheet.xlsx")) == expected_dict

def test_get_requested_metals_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_requested_metals("non-existent.xlsx")


def test_move_data():
    with pytest.raises(FileNotFoundError):
        move_data(get_sample_data(get_raw_data("raw data.xlsx")), get_requested_metals("test_excel_sheet.xlsx"), "non-existent.xlsx")



if __name__ == "__main__":
    main()
