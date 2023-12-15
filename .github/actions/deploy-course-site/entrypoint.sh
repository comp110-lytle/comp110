#!/bin/bash

SRC_DIR=${1}
TARGET_REPO_USER_ORG=${2}
TARGET_REPO_NAME=${3}
TARGET_REPO="https://${API_TOKEN_GITHUB}@github.com/${TARGET_REPO_USER_ORG}/${TARGET_REPO_NAME}"
CLONE_PATH="/__${TARGET_REPO_NAME}__"

main() {
    check_args_and_env $@
    git_config
    git_clone "${TARGET_REPO}" "${CLONE_PATH}"
    rm_all_except_hidden_in "${CLONE_PATH}"
    cp -r "${SRC_DIR}/." "${CLONE_PATH}"
    pandoc_md_to_html "${CLONE_PATH}"
    git_add_all_and_commit "${CLONE_PATH}"
}

check_args_and_env() {
    if [[ "${#}" != 3 ]]; then
        print_stderr "Expected Arguments: [SRC_DIR] [GH_TARGET_REPO_USER] [GH_TARGET_REPO_NAME]"
        exit 1
    fi

    if [[ "${API_TOKEN_GITHUB}" == "" ]]; then
        printenv
        print_stderr "Expected Environment Variable: API_TOKEN_GITHUB"
        print_stderr "This should be set to a Github Access Token"
        exit 1
    fi
}

print_stderr() {
    # Usage: print_stderr "message"
    echo "$1" >&2
}

git_config() {
    git config --global user.email "kris@cs.unc.edu"
    git config --global user.name "$TARGET_REPO_USER_ORG"
}

git_clone() {
    # Usage: git_clone [URL] [target]
    git clone --depth 1 "${1}" "${2}"
}

rm_all_except_hidden_in() {
    # Usage: rm_all_except_hidden_in [path]
    pushd "${1}" >/dev/null
    # delete all files except hidden files in root (especially: .git)
    find . | grep -v -E "^\..*$" | xargs rm -rf
    popd >/dev/null
}

pandoc_md_to_html() {
    python3 -m pip install jinja2
    pushd "${1}" >/dev/null
    local opts="--standalone --template=layout.html --toc --toc-depth=3"
    find . | grep -E "\.md$" | sed 's/\.md$//' | xargs -I {} python3 -m prod {}  # pandoc $opts -o {}.html {}.md
    find . | grep -E "\.md$"| xargs rm -rf
    rm layout.html
    popd >/dev/null
}

git_add_all_and_commit() {
    # Usage: git_add_all_and_commit [repo path]
    pushd "${1}" >/dev/null
    if [ -n "$(git status --porcelain)" ]; then
        git add .
        git commit --message "Mirroring upstream changes."
        git push origin main
    else
        echo "No changes in downstream repository."
    fi
    popd >/dev/null
}

main $@