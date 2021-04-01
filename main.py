from screenshooter import ScreenShooter
from argparse import ArgumentParser


def main(url: str, branch_name: str) -> None:
    screenShooter = ScreenShooter(url=url, branch_name=branch_name)
    screenShooter.download_dir()
    screenShooter.take_screenshots()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--git-link")
    parser.add_argument("--branch-name")
    args = parser.parse_args()
    url = args.git_link
    branch_name = args.branch_name
    main(url=url, branch_name=branch_name)
