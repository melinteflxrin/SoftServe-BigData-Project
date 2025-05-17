import subprocess
import sys
import os

def run_etl_and_dashboard(num_users, num_days, db_host, db_port, db_user, db_pass, db_name, usda_api_key):
    """
    run ETL and dashboard scripts with user's parameters.
    """
    extract_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'extract', 'healthapp.py'))
    transform_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'transform', 'transform.py'))
    load_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'load', 'load.py'))
    dashboard_script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dashboard', 'dashboard.py'))

    env = os.environ.copy()
    env["DB_HOST"] = db_host
    env["DB_PORT"] = str(db_port)
    env["DB_USER"] = db_user
    env["DB_PASSWORD"] = db_pass
    env["DB_NAME"] = db_name
    env["USDA_API_KEY"] = usda_api_key

    subprocess.run([
        sys.executable, extract_script,
        "--users", str(num_users),
        "--days", str(num_days)
    ], check=True, env=env)
    subprocess.run([sys.executable, transform_script], check=True, env=env)
    subprocess.run([sys.executable, load_script], check=True, env=env)
    subprocess.run([sys.executable, dashboard_script], check=True, env=env)