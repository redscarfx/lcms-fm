from __future__ import annotations

from pathlib import Path

from foundation.data.download.massive import parse_params_xml
from tqdm import tqdm
from foundation.data.download.downloader import (
    download_file,
    setup_download_logger,
)
from foundation.data.metadata.extractor import extract_metadata
from foundation.data.metadata.writer import (
    append_metadata_csv,
    append_metadata_parquet,
)

ACCESSION = "MSV000096884"

PROJECT_DATA = Path("data") / ACCESSION

OUTPUT_ROOT = Path("/temporary/2025-2026/21316700/lcms-fm/data")


def main() -> None:
    params_xml = PROJECT_DATA / "params.xml"

    entries = parse_params_xml(
        accession=ACCESSION,
        params_xml=params_xml,
    )

    print("=" * 80)
    print("MassIVE Downloader")
    print("=" * 80)

    print(f"Dataset : {ACCESSION}")
    print(f"Found   : {len(entries)} mzML files")
    print()

    downloaded = 0
    skipped = 0
    log_file = PROJECT_DATA / "download.log"
    csv_path = PROJECT_DATA / "metadata.csv"
    parquet_path = PROJECT_DATA / "metadata.parquet"
    download_logger = setup_download_logger(log_file)

    for entry in tqdm(
        entries,
        desc="Files",
        unit="file",
    ):
        download_logger.info(
            "Downloading %s",
            entry.relative_path,
        )
        output_path = download_file(
            entry=entry,
            output_root=OUTPUT_ROOT,
        )

        metadata = extract_metadata(
            accession=ACCESSION,
            relative_path=entry.relative_path,
            mzml_path=output_path,
        )

        download_logger.info(
            "SUCCESS %s",
            output_path,
        )

        append_metadata_csv(
            metadata,
            csv_path,
        )

        append_metadata_parquet(
            metadata,
            parquet_path,
        )

        if output_path.exists():
            downloaded += 1
        else:
            skipped += 1

    print()
    print("=" * 80)
    print("Download finished")
    print("=" * 80)
    print(f"Downloaded : {downloaded}")
    print(f"Skipped     : {skipped}")
    print(f"Output root : {OUTPUT_ROOT / ACCESSION}")


if __name__ == "__main__":
    main()
