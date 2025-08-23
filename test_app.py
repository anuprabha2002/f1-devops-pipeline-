def test_output():
    import subprocess
    result = subprocess.run(['python3', 'app.py'], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello DevOps", "App output is wrong!"

if __name__ == "__main__":
    test_output()
    print("Test passed ✅")

