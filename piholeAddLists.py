
PARAM_LIST = 'list'
PARAM_VERBOSE = 'verbose'


def main(argv):
    global isVerbose

    print('######### GET SCRUM DATA #########')

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--'+PARAM_LIST, help="list referencing every list to add", required=True)
    parser.add_argument('-l', '--'+PARAM_SHORTENED_LOGS, help="is short logs needed", required=False, action='store_true')
    parser.add_argument('-v', '--'+PARAM_VERBOSE,   help="needs to display every HTTP call",  required=False, action='store_true')
    args = parser.parse_args()
