from mylib.lib import (
    read_csv_data,
    generate_summary_stats,
    generate_bar_chart_for_most_popular_artists,
    generate_markdown,
    generate_reports
)


def main():
    csv_file_name = "spotify-2023.csv"
    spotify_df = read_csv_data(csv_file_name)
    summary_stats = generate_summary_stats(spotify_df)
    print(summary_stats)

    generate_markdown(csv_file_name)
    generate_reports(csv_file_name)
    generate_bar_chart_for_most_popular_artists(csv_file_name)


if __name__ == "__main__":
    main()
