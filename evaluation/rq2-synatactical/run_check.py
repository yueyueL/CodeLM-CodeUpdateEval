import pandas as pd
import numpy as np
import os
import multiprocessing
import tempfile


def analyze_file(prediction, pmd_dir):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_code = os.path.join(temp_dir, "temp.java")
        report_path = os.path.join(temp_dir, "report.txt")

        with open(temp_code, "w") as f:
            f.write("public class TempSnippet {\n")
            f.write("  " + prediction + "\n")
            f.write("}\n")

        os.chdir(pmd_dir)
        os.system(f"pmd check -d {temp_code} -R rulesets/java/basic.xml -f text -r {report_path}")
        with open(report_path, "r") as f:
            report = f.read()
        return report.replace("\n", " ")

def run_pmd_java():
    data_types = ["android", "google", "ovirt"]
    scenarios = ["dataset-time-ignore", "dataset-time-wise"]
    models = ["codet5", "codet5p", "tufanoT5", "codebert", "codegpt", "unixcoder", "autotransform"]

    for data_type in data_types:
        for scenario in scenarios:
            for model in models:
                test_dir = f"path/to/your/test/directory/{scenario}/{data_type}/{model}/"
                test_path = os.path.join(test_dir, "predictions_beam_1.txt")
                saved_result_path = os.path.join(test_dir, "pmd_results.txt")

                pmd_dir = "path/to/your/pmd/directory"

                with open(test_path, "r") as f:
                    predictions = f.readlines()
                predictions = [x.strip() for x in predictions]

                pool = multiprocessing.Pool(processes=20)
                final_results = pool.map(analyze_file, [(prediction, pmd_dir) for prediction in predictions])
                pool.close()
                pool.join()

                with open(saved_result_path, "w") as f:
                    for result in final_results:
                        f.write(result + "\n")

def run_pmd_java_android():
    scenarios = ["3_1"]
    models = ["transformer_hparams8"]

    for scenario in scenarios:
        for model in models:
            test_dir = f"path/to/your/test/directory/{scenario}/{model}/"
            test_path = os.path.join(test_dir, "predictions_beam_1.txt")
            saved_result_path = os.path.join(test_dir, "pmd_results.txt")

            with open(test_path, "r") as f:
                predictions = f.readlines()
            predictions = [x.strip() for x in predictions]

            pool = multiprocessing.Pool(processes=15)
            final_results = pool.map(analyze_file, [(prediction, "path/to/your/pmd/directory") for prediction in predictions])
            pool.close()
            pool.join()

            with open(saved_result_path, "w") as f:
                for result in final_results:
                    f.write(result + "\n")

def output_performance():
    data_types = ["android", "google", "ovirt"]
    scenarios = ["dataset-time-ignore", "dataset-time-wise"]
    models = ["codet5", "codet5p", "tufanoT5", "codebert", "codegpt", "unixcoder", "autotransform"]

    for data_type in data_types:
        for scenario in scenarios:
            for model in models:
                test_dir = f"path/to/your/test/directory/{scenario}/{data_type}/{model}/"
                saved_result_path = os.path.join(test_dir, "pmd_results.txt")
                with open(saved_result_path, "r") as f:
                    results = f.readlines()
                total = len(results)
                count = sum(1 for result in results if result.strip() == "")
                print(data_type, scenario, model, count / total, total, count)

    scenarios = ["3_1", "3_no"]
    models = ["codet5", "codet5p", "t5", "codebert", "codegpt", "unixcoder", "transformer_hparams8"]
    for scenario in scenarios:
        for model in models:
            test_dir = f"path/to/your/test/directory/{scenario}/{model}/"
            saved_result_path = os.path.join(test_dir, "pmd_results.txt")
            with open(saved_result_path, "r") as f:
                results = f.readlines()
            total = len(results)
            count = sum(1 for result in results if result.strip() == "")
            print("android", scenario, model, count / total, total, count)

if __name__ == "__main__":
    run_pmd_java_android()