import os


RESULTS_DIR = "test_results"
TEST_ID = os.environ.get("CCM_TEST_ID", None)
SCYLLA_DOCKER_IMAGE = os.environ.get(
    "SCYLLA_DOCKER_IMAGE", "scylladb/scylla-nightly:666.development-0.20201015.8068272b466")
SCYLLA_RELOCATABLE_VERSION = "unstable/master:2025-01-19T09:39:05Z"

# Feb/8 comment to refresh the action cache
