from pathlib import Path

from foundation.data.download.massive import parse_params_xml


def main() -> None:
    accession = "MSV000096884"

    params_xml = Path("data") / accession / "params.xml"

    entries = parse_params_xml(
        accession=accession,
        params_xml=params_xml,
    )

    print("=" * 80)
    print("MassIVE Parser")
    print("=" * 80)

    print(f"Dataset : {accession}")
    print(f"Found   : {len(entries)} mzML files")

    assert entries, "No mzML files found."

    print("\nFirst entry")
    print(entries[0])

    print("\nLast entry")
    print(entries[-1])

    assert len(entries) == len({e.relative_path for e in entries})

    assert entries == sorted(
        entries,
        key=lambda e: e.relative_path,
    )

    print("\nParser validation: OK")


if __name__ == "__main__":
    main()
