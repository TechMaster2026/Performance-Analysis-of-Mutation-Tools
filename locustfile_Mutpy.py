import subprocess
import logging
import time
from locust import User, task, events

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class MutPyStressUser(User):
    wait_time = lambda self: 1  

    @task
    def run_mutation_test(self):
        """Execute MutPy and log performance metrics."""
        start_time = time.time()

        try:
            result = subprocess.run(
            [
            "python",
            "C:\\Users\\priya\\AppData\\Roaming\\Python\\Python310\\Scripts\\mut.py",
            "--target", "BankApplication",
            "--unit-test", "test_BankApplication"
            ],
            capture_output=True, text=True, check=True
            )
            duration = (time.time() - start_time) * 1000  # Convert to ms
            logging.info("MutPy executed successfully in %.2f ms!", duration)

            self.environment.events.request.fire(
                request_type="EXECUTE",
                name="MutPy Execution",
                response_time=duration,
                response_length=len(result.stdout) if result.stdout else 0,
                context={},
                exception=None
            )

        except subprocess.CalledProcessError as e:
            logging.error("MutPy execution failed! Error: %s", e.stderr)
            self.environment.events.request.fire(
                request_type="EXECUTE",
                name="MutPy Execution",
                response_time=0,
                response_length=0,
                context={},
                exception=e
            )

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Starts the mutation testing when Locust begins."""
    logging.info("Starting MutPy Stress Test with Locust!")
