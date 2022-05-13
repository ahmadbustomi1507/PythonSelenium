import sys
sys.path.append('.')
import os
import subprocess
import argparse
from datetime import datetime
import pathlib
import uuid
import  time
from src.tools import utility as ut
import shutil

# def get_unique_run_id():
#     generated_uuid = uuid.uuid4()
#     date_time      = datetime.now().strftime('%Y%m%d%H%M%S')
#     unique_run_id =  "_{}_{}".format(unique_build_number,date_time)
#     os.environ['UNIQUE_RUN_ID'] = unique_run_id
#     return unique_run_id

def get_work_directory():
    return pathlib.Path(__file__).parent.absolute()

def get_test_feature(test_suite_path='',project_name='',feature_name='.'):
    return os.path.join(*[test_suite_path,project_name,feature_name])

if __name__ == '__main__':


    #----------------------------------------------------------------------------------------
    print("Initialize Parser Definition")
    #----------------------------------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('--tags', type=str, required=False,
                        help="Options in behave")
    parser.add_argument('--project_name',type=str,required=True,
                        help='Basically the folder inside the test_suite_bdd, please choose one')
    parser.add_argument('--feature_name',type=str,required=False,
                        help='*.feature name inside the project name',default='.')
    parser.add_argument('--unique',type=str,required=True,
                        help='unique number for folder result naming')
    parser.add_argument('--behave_options', type=str, required=False,
                        help='some additional behave options')

    #----------------------------------------------------------------------------------------
    print("Parsing the args")
    #----------------------------------------------------------------------------------------
    args                    = parser.parse_args()
    tags_name               = args.tags
    project_name            = args.project_name
    feature_name            = args.feature_name
    unique_name             = args.unique

    #----------------------------------------------------------------------------------------
    print("Processing the args")
    #----------------------------------------------------------------------------------------
    #current directory / runner.py directory
    workdir = get_work_directory()

    #src directory
    src_dir         = os.path.join(workdir, 'src')

    # get output_dir
    results_dir     = os.path.join(workdir,'results')
    try:
        os.mkdir(results_dir)
    except FileExistsError as err:
        print(f"File already exist, no need to recreate the dir {results_dir}")

    # get test_suites directory
    test_suite_dir  = os.path.join(src_dir,'test_suite_bdd')

    # create output directory for log
    log_dir         = os.path.join(results_dir,f'{unique_name}')

    # create summary directory for generated allure report
    summary_dir         = os.path.join(results_dir,f'{unique_name}_summary')

    #----------------------------------------------------------------------------------------
    print("Process the full path of the feature")
    #----------------------------------------------------------------------------------------
    test_feature_name = get_test_feature(test_suite_path=test_suite_dir,project_name=project_name,feature_name=feature_name)
    #----------------------------------------------------------------------------------------
    print(f"Execute the feature : {test_feature_name}")
    #----------------------------------------------------------------------------------------

    command =   f'behave -f allure_behave.formatter:AllureFormatter -f pretty ' \
                f'-o {log_dir} ' \
                f'{test_feature_name} ' \
                f'--no-capture ' \
                f'--tags {tags_name} '

    try:
        # Running command and then generate log
        print(f"Running command: {command}")
        rs = subprocess.run(command, shell=True)

        # TO DO :12-05-2022 (eksplisit wait)
        time.sleep(5)

        # Generate Report
        print(f"Generate Report Summary to directory: {summary_dir}")
        command = f'allure generate {log_dir} -o {summary_dir}'
        print(f"Running command: {command}")
        rs = subprocess.run(command, shell=True)

        # TO DO :12-05-2022
        time.sleep(5)

        # Generate one html
        print(f"Generate One Html Report to directory: {results_dir}")
        html_single_summary = Ut.combine(src=summary_dir, dest=results_dir)
        print(f'html_single_summary = {html_single_summary}')

        # TO DO :12-05-2022
        time.sleep(10)

    except Exception as err:
        raise Exception(f"Ada error di runner, harus di cek,{type(err)} ")
        print (f"Ada error, harus di cek,{type(err)} ")

    finally:
        print(f"Delete the folder : {results_dir}")
        shutil.rmtree(path=log_dir,ignore_errors=True)
        shutil.rmtree(path=summary_dir,ignore_errors=True)