import os
import shutil
import subprocess
import logging
import time
import random
import uuid
from locust import User, task, events

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class MutationTestingUser(User):
    """Simulates a Locust user executing Mutatest stress tests."""

    wait_time = lambda self: random.uniform(5, 10)  #Controlled execution intervals

    @task
    def run_mutatest_test(self):
        """Execute Mutatest with isolated copies per user."""
        time.sleep(random.uniform(1, 5))  #Prevent all users from starting at the same time

        unique_id = uuid.uuid4().hex[:8]  #Unique temp dir for each user
        temp_dir = f"mutatest_temp_{unique_id}"

        try:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)  #Ensure clean environment

            os.makedirs(temp_dir, exist_ok=True)
            shutil.copy("BankApplication.py", f"{temp_dir}/BankApplication.py")

            self.run_mutation_test(
                "Mutatest Execution",
                [
                    "mutatest",
                    "-s", f"{temp_dir}/BankApplication.py",
                    "-n", "8",
                    "-m", "s",  #Only test surviving mutations
                    "--parallel"  # Run in parallel mode safely
                ]
            )

        except Exception as e:
            logging.error("Error setting up Mutatest environment: %s", str(e))

        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)  #Clean up temp files after execution

    def run_mutation_test(self, test_name, command):
        """Generic method to run mutation tests and log performance."""
        start_time = time.time()

        try:
            result = subprocess.run(
                command, capture_output=True, text=True, check=True
            )
            duration = (time.time() - start_time) * 1000  # Convert to milliseconds
            logging.info("%s completed in %.2f ms!", test_name, duration)

            self.environment.stats.log_request(
                method="GET",
                name=test_name,
                response_time=duration,
                content_length=len(result.stdout) if result.stdout else 0
            )

        except subprocess.CalledProcessError as e:
            logging.error("%s failed!\nSTDOUT:\n%s\nSTDERR:\n%s", test_name, e.stdout, e.stderr)
            self.environment.stats.log_error(self, test_name, e)

        except Exception as e:
            logging.error("Unexpected error in %s: %s", test_name, str(e))


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Log when the test starts."""
    logging.info("Starting Mutatest Stress Test with Locust!")
