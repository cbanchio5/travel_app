interface AuthInput {
  email: string;
  password: string;
  username: string
}

export async function login(data: AuthInput) {
  const res = await fetch('/auth/login/`', {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error("Login failed");
  }

  return await res.json(); // token, user info, etc.
}

export async function signup(data: AuthInput) {
  const res = await fetch('/auth/login/', {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error("Signup failed");
  }

  return await res.json();
}
