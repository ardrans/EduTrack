PERMISSIONS = {
    "add_user": ["hr"],
    "manage_roles": ["hr"],
    "view_reports": ["hr", "trainer"],
}

from flask import jsonify, g

def check_permission(action):
    """
    Check if the current user's role has permission for the given action.
    :param action: The action to check (e.g., 'add_user', 'manage_roles').
    :return: None if authorized, otherwise a JSON response with an error.
    """
    # Fetch the current user from Flask's `g` object
    user = g.user

    # Fetch allowed roles for the action
    allowed_roles = PERMISSIONS.get(action, [])
    if user.role.name.lower() not in [role.lower() for role in allowed_roles]:
        return jsonify({"error": f"Permission denied. Allowed roles: {', '.join(allowed_roles)}"}), 403

    return None