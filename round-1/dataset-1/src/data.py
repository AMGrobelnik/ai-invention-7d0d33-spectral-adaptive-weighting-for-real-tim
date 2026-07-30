#!/usr/bin/env python3
"""Convert time series dataset to exp_sel_data_out.json schema (selected datasets only)."""

import json
import sys
from pathlib import Path
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1")

# Best 4 datasets selected for spectral-adaptive ensemble research
SELECTED_DATASETS = {
    "transportation": "PEMS traffic with regime shifts",
    "energy": "Electricity with seasonal patterns",
    "weather": "Temperature with diurnal cycles",
    "finance": "Stock prices with trend/volatility"
}

@logger.catch(reraise=True)
def convert_to_schema():
    """Load data_out.json and convert to exp_sel_data_out.json schema (selected only)."""

    # Load input dataset
    input_file = WORKSPACE / "data_out.json"
    logger.info(f"Loading {input_file}")

    with open(input_file) as f:
        input_data = json.load(f)

    logger.info(f"Loaded {input_data['count']} series total")

    # Group by domain, filter to selected only
    datasets_dict = {}

    for series in input_data['series']:
        domain = series['domain']

        # Only include selected datasets
        if domain not in SELECTED_DATASETS:
            continue

        if domain not in datasets_dict:
            datasets_dict[domain] = []

        # Create example: each time series is one example
        example = {
            "input": json.dumps(series['values_train']),
            "output": series['frequency'],
            "metadata_series_id": series['series_id'],
            "metadata_domain": series['domain'],
            "metadata_frequency": series['frequency'],
            "metadata_series_length": series['series_length'],
            "metadata_source": series['source'],
            "metadata_train_end_idx": series['train_end_idx'],
            "metadata_train_mean": round(series['metadata']['train_stats']['mean'], 4),
            "metadata_train_std": round(series['metadata']['train_stats']['std'], 4),
            "metadata_spectral_power_ratio": round(series['metadata']['train_stats']['spectral_power_ratio'], 4),
            "metadata_test_values": json.dumps(series['values_test']),
            "metadata_row_index": len(datasets_dict[domain]),
        }

        datasets_dict[domain].append(example)

    # Convert to output schema
    output_data = {
        "datasets": [
            {
                "dataset": dataset_name,
                "examples": examples
            }
            for dataset_name, examples in sorted(datasets_dict.items())
        ]
    }

    logger.info(f"Selected {len(output_data['datasets'])} dataset groups")
    total_examples = sum(len(ds['examples']) for ds in output_data['datasets'])
    for ds in output_data['datasets']:
        logger.info(f"  {ds['dataset']:20} | {len(ds['examples']):3d} examples")

    # Save output
    output_file = WORKSPACE / "full_data_out.json"
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    logger.info(f"Saved to {output_file}")
    file_size_mb = output_file.stat().st_size / (1024 * 1024)
    logger.info(f"Output file size: {file_size_mb:.2f} MB")

    return output_data

if __name__ == "__main__":
    Path("logs").mkdir(exist_ok=True)
    output = convert_to_schema()
    total_ex = sum(len(ds['examples']) for ds in output['datasets'])
    logger.info(f"Conversion complete: {len(output['datasets'])} datasets, {total_ex} total examples")
