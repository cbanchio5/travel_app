import { useState } from "react";
import { login } from "../../services/authService";

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await login({ email, password, username });
      // redirect to dashboard
    } catch (error) {
      alert("Login failed");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-sm">
      <input
        type="email"
        value={email}
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
        className="input mb-2"
      />
        <input
        type="username"
        value={password}
        placeholder="username"
        onChange={(e) => setUsername(e.target.value)}
        className="input mb-2"
      />
      <input
        type="password"
        value={password}
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        className="input mb-2"
      />
      <button type="submit" className="btn">Login</button>
    </form>
  );
}
