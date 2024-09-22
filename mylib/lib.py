import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport


def read_csv_data(filename):
    return pd.read_csv(filename, encoding="latin-1")


def generate_summary_stats(df: pd.DataFrame):
    return df.describe()


def generate_bar_chart_for_most_popular_artists(filename):
    df = read_csv_data(filename)

    df["streams"] = pd.to_numeric(df["streams"], errors="coerce")
    df.dropna(subset=["streams"], inplace=True)

    # Create bar chart for 10 hottest songs reflected in stream counts
    top_artists = df.groupby("artist(s)_name")["streams"].sum().nlargest(10)
    plt.figure(figsize=(10, 6))
    top_artists.plot(kind="bar", color="blue")
    plt.title("10 Hottest Artists by Total Stream Count")
    plt.xlabel("Artists")
    plt.ylabel("Total Streams")
    plt.xticks(rotation=45)
    plt.show()


def generate_summary_for_stream_count(filename):
    df = read_csv_data(filename)

    df["streams"] = pd.to_numeric(df["streams"], errors="coerce")
    df.dropna(subset=["streams"], inplace=True)

    stream_median = df["streams"].median()
    stream_max = df["streams"].max()
    stream_min = df["streams"].min()
    return (stream_median, stream_max, stream_min)


def generate_markdown(filename):
    info1, info2, info3 = generate_summary_for_stream_count(filename)
    info1 = str(info1)
    info2 = str(info2)
    info3 = str(info3)

    with open("stream_count_summary.md", "w", encoding="utf-8") as file:
        file.write("Median:\n")
        file.write(info1)
        file.write("\n\n")
        file.write("Max:\n")
        file.write(info2)
        file.write("\n\n")
        file.write("Min:\n")
        file.write(info3)


def generate_reports(filename):
    df = read_csv_data(filename)
    profile = ProfileReport(df, title="Spotify Streaming Data 2023")
    profile.to_file("spotify_data.html")