from mylib.lib import (
    read_csv_data,
    generate_summary_for_stream_count,
)
csv_file_name = "spotify-2023.csv"


def test_loading_csv_data():
    df = read_csv_data(csv_file_name)
    assert df is not None
    assert df.shape == (953, 24)


def test_stream_count_summary():
    summary_stats = generate_summary_for_stream_count(csv_file_name)
    assert summary_stats is not None

    median, max, min = summary_stats
    assert median == 290530915.0
    assert max == 3703895074.0
    assert min == 2762.0


if __name__ == "__main__":
    test_loading_csv_data()
    test_stream_count_summary()
