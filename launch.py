import argparse

parser = argparse.ArgumentParser(description='Launch EQA environment')
parser.add_argument('-src', '--source', type=str, metavar='', help="Filepath of source files")
parser.add_argument('-wrk', '--working', metavar='', type=str, help="Filepath of working files")
parser.add_argument('-g', '--gloss', metavar='', type=str, help="Filepath of glossary as string")
parser.add_argument('-dnt', '--dnt', metavar='', type=str, help="Filepath of do not translate terms (DNT)")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()


class Launcher:
    def __init__(self, source=None, working=None, glossary=None, dnt=None, *unused):
        self.source = source
        self.working = working
        self.glossary = glossary
        self.dnt = dnt

    def execute(self):
        if args.quiet:
            print(f"Source: {self.source}")
            print(f"Working: {self.working}")
            print(f"Glossary: {self.glossary}")
            print(f"DNT: {self.dnt}")
        elif args.verbose:
            print(f"Source files path is {self.source}")
            print(f"Working files path is {self.working}")
            print(f"Glossary file path is {self.working}")
            print(f"DNT file path is {self.dnt}")


if __name__ == "__main__":
    print(vars(args))
    launcher = Launcher(*vars(args))
    launcher.execute()
