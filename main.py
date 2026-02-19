import argparse
from monitor.core import NetworkMonitor
from monitor.utils import validate_target


def get_args():
    parser = argparse.ArgumentParser(
        description="Simple Network Monitoring Tool"
    )

    parser.add_argument("-t", "--targets", nargs="+", required=True,
                        help="List of targets to monitor")

    parser.add_argument("-p", "--port", type=int,
                        help="Optional port to check")

    parser.add_argument("-i", "--interval", type=int, default=5,
                        help="Check interval in seconds")

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    valid_targets = [t for t in args.targets if validate_target(t)]

    if not valid_targets:
        print("No valid targets provided.")
        exit(1)

    monitor = NetworkMonitor(
        targets=valid_targets,
        port=args.port,
        interval=args.interval
    )

    monitor.start()
