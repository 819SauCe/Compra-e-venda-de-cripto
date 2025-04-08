try:
    from sklearn import linear_model
    from sklearn import datasets
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    from openai import OpenAI
    from dotenv import load_dotenv
    import os
    from supabase import create_client, Client
except ImportError as e:
    print(f"Error importing modules: {e}")
    os.system(f'pip install {e.name}')
    exit(1)

def main():
    url: str = os.environ.get("SUPA_BASE_URL")
    key: str = os.environ.get("SUPA_BASE_KEY")
    supabase: Client = create_client(url, key)

    def execut_calc():
        result = supabase.table("Cripto").select("*", count="exact").execute()
        lines = result.count
        print(lines)

        for line in range(lines):
            cripto_line = result.data[line]
            print(cripto_line)

    execut_calc()