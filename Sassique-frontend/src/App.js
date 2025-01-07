// src/App.js
import React, { Suspense, lazy } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
} from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";

// Lazy load pages
const Home = lazy(() => import("./pages/Home"));
const Login = lazy(() => import("./components/Login"));
const NotFound = lazy(() => import("./pages/NotFound"));
const Cart = lazy(() => import("./pages/cart"));
const Wishlist = lazy(() => import("./pages/wishlist"));
const Bestseller = lazy(() => import("./pages/bestseller"));
const NewArrival = lazy(() => import("./pages/Newarrival"));
const Product = lazy(() => import("./pages/product"));
const Signup = lazy(() => import("./pages/signup"));
const PasswordResetPage = lazy(() => import("./pages/PasswordResetPage"));
const SocialLogin = lazy(() => import("./pages/SocialLogin")); // Ensure this is exported as default

// Logout function using useNavigate
const Logout = () => {
  const navigate = useNavigate();
  localStorage.clear();
  navigate("/login");
  return null;
};

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Home />
              </ProtectedRoute>
            }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/wishlist" element={<Wishlist />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/bestseller" element={<Bestseller />} />
          <Route path="/newarrival" element={<NewArrival />} />
          <Route path="/product" element={<Product />} />
          <Route path="/passwordreset" element={<PasswordResetPage />} />
          <Route path="/sociallogin" element={<SocialLogin />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

export default App;
