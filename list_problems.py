import os

LANG_DIRS = ["Java", "MySQL", "Python", "Python3", "Swift"]
OUTPUT_FILE = "problem_tree.txt"
README_FILE = "README.md"


def list_problem_tree(base_path="."):
    tree_lines = []
    problem_paths = []
    for lang in LANG_DIRS:
        lang_path = os.path.join(base_path, lang)
        if not os.path.isdir(lang_path):
            continue
        for site in sorted(os.listdir(lang_path)):
            site_path = os.path.join(lang_path, site)
            if not os.path.isdir(site_path):
                continue
            for level in sorted(os.listdir(site_path)):
                level_path = os.path.join(site_path, level)
                if not os.path.isdir(level_path):
                    continue
                for problem in sorted(os.listdir(level_path)):
                    problem_path = os.path.join(level_path, problem)
                    if os.path.isdir(problem_path):
                        # 체크박스용 경로 생성
                        rel_path = f"{lang}/{site}/{level}/{problem}"
                        problem_paths.append(rel_path)
                        # 트리 구조도 기존대로 저장
                        tree_lines.append(f"      {problem}/")
    return tree_lines, problem_paths


def append_checkbox_to_readme(problem_paths, readme_path=README_FILE):
    checkbox_lines = [f"- [ ] {path}" for path in problem_paths]
    checkbox_str = '\n'.join(checkbox_lines)
    # --- 마커로 감싸기
    marker_block = f"\n---\n{checkbox_str}\n---\n"
    # README.md가 없으면 새로 생성
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(marker_block)
        print(f"README.md가 없어서 새로 만들고 체크박스 목록을 추가했습니다.")
        return
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
    if checkbox_str.strip() in readme_content:
        print("README.md에 이미 동일한 체크박스 목록이 있어 추가하지 않습니다.")
        return
    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(marker_block)
    print("README.md 맨 아래에 체크박스 목록을 추가했습니다.")


def main():
    tree_lines, problem_paths = list_problem_tree()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in tree_lines:
            f.write(line + "\n")
    print(f"문제 트리 구조가 {OUTPUT_FILE} 파일에 저장되었습니다.")
    append_checkbox_to_readme(problem_paths)


if __name__ == "__main__":
    main() 