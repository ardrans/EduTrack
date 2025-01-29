import { createContext } from "react";

const AuthContext = createContext({
  user: null,
  isAuthenticated: false,
  handleLogout: () => {},
});

export default AuthContext;
