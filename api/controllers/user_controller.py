from flask import Blueprint, request


@user_controller.route("/user/add", methods=['POST'])
def user_add():
    return 'ok'