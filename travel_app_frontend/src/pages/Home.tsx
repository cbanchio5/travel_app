import LoginForm from "../components/Auth/LoginForm";
import SignupForm from "../components/Auth/SignUpForm";
import { useState } from "react";

export default function Home() {
  const [showLogin, setShowLogin] = useState(true);

  return (
    
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-tr from-blue-100 via-white to-blue-100 p-6">
      <div className="bg-red-500 text-white p-4">Test Tailwind</div>
      <h1 className="text-4xl font-extrabold mb-8 text-blue-900 drop-shadow-lg">
        Trippy ok
      </h1>
      
      <div className="w-full max-w-md bg-white rounded-xl shadow-lg p-8">
        {showLogin ? <LoginForm /> : <SignupForm />}
      </div>
      
      <button
        onClick={() => setShowLogin(!showLogin)}
        className="mt-6 text-sm text-blue-700 hover:text-blue-900 underline transition-colors duration-300"
      >
        {showLogin ? "Don't have an account? Sign up" : "Already have an account? Log in"}
      </button>
    </div>
  );
}
