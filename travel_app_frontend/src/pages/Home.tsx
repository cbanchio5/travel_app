import LoginForm from "../components/Auth/LoginForm";
import SignupForm from "../components/Auth/SignUpForm";
import { useState } from "react";

export default function Home() {
  const [showLogin, setShowLogin] = useState(true);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <h1 className="text-3xl font-bold mb-6">Welcome to Trip Planner</h1>
      {showLogin ? <LoginForm /> : <SignupForm />}
      <button
        onClick={() => setShowLogin(!showLogin)}
        className="mt-4 text-sm text-blue-600 underline"
      >
        {showLogin ? "Don't have an account? Sign up" : "Already have an account? Log in"}
      </button>
    </div>
  );
}
