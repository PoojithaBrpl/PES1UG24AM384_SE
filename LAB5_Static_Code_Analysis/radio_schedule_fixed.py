"""Manage a simple in-memory radio show schedule."""

import sqlite3


def add_slot(connection, show, host, start_hour, minutes):
    """Add a radio show to the schedule."""
    connection.execute(
        """
        INSERT INTO slots (show, host, start_hour, minutes)
        VALUES (?, ?, ?, ?)
        """,
        (show, host, start_hour, minutes),
    )


def slot_label(show, host):
    """Return a formatted label for a radio show."""
    return f"{show} hosted by {host}"


def overlap_free(start_hour, minutes, other_start, other_minutes):
    """Return whether two radio show time slots do not overlap."""
    end_hour = start_hour + minutes / 60
    other_end = other_start + other_minutes / 60

    return end_hour <= other_start or other_end <= start_hour


def morning_shows(connection):
    """Return the names of shows starting before noon."""
    cursor = connection.execute(
        "SELECT show FROM slots WHERE start_hour < 12"
    )
    return [row[0] for row in cursor.fetchall()]


def remove_slot(connection, slot_id):
    """Remove a radio show using its slot ID."""
    connection.execute("DELETE FROM slots WHERE id = ?", (slot_id,))


def main():
    """Run the radio schedule demonstration."""
    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            """
            CREATE TABLE slots (
                id INTEGER PRIMARY KEY,
                show TEXT,
                host TEXT,
                start_hour INTEGER,
                minutes INTEGER
            )
            """
        )

        add_slot(connection, "Sunrise Beats", "Vik", 7, 60)
        add_slot(connection, "Midday Talk", "Anu", 13, 45)

        print(slot_label("Sunrise Beats", "Vik"))
        print(
            overlap_free(7, 60, 13, 45),
            morning_shows(connection),
        )

        remove_slot(connection, 2)


if __name__ == "__main__":
    main()
