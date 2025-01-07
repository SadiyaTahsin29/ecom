import React from 'react';
import { SocialLogin } from './SocialLogin';  // Import the SocialLogin component

const SignIn = () => {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center relative">
      {/* Logo outside container */}
      <div className="absolute top-2 left-2">
        <img src="pics/logo.png" alt="Logo" className="w-20 h-20" />
      </div>

      <div className="bg-white w-full max-w-lg p-8 rounded-xl shadow-lg border-4 border-teal-600">
        
        <div className="flex justify-center mb-4">
          <img src="pics/logo.png" alt="Logo" className="w-16 h-16" />
        </div>

        <h2 className="text-center text-2xl font-bold text-teal-600 mb-6 font-serif">Sign Up</h2>

        <form>
          {/* Email/Phone */}
          <div className="mb-4">
            <label htmlFor="email" className="sr-only">Email / Phone</label>
            <input type="text" id="email" placeholder="Email / Phone"
              className="w-4/5 px-4 py-2 border-2 border-teal-600 rounded-md mx-auto block focus:outline-none focus:ring-2 focus:ring-teal-300" />
          </div>

          {/* Password */}
          <div className="mb-4">
            <label htmlFor="password" className="sr-only">Password</label>
            <input type="password" id="password" placeholder="Password"
              className="w-4/5 px-4 py-2 border-2 border-teal-600 rounded-md mx-auto block focus:outline-none focus:ring-2 focus:ring-teal-300" />
          </div>

          {/* Confirm Password */}
          <div className="mb-6">
            <label htmlFor="confirm-password" className="sr-only">Confirm Password</label>
            <input type="password" id="confirm-password" placeholder="Confirm Password"
              className="w-4/5 px-4 py-2 border-2 border-teal-600 rounded-md mx-auto block focus:outline-none focus:ring-2 focus:ring-teal-300" />
          </div>

          {/* Continue Button */}
          <button type="submit"
            className="w-2/5 h-12 bg-teal-500 text-white rounded-lg font-medium text-lg mx-auto block hover:bg-teal-600 active:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-300">
            Continue
          </button>
        </form>

        {/* Divider */}
        <div className="flex items-center my-6">
          <div className="border-t flex-grow border-gray-300"></div>
          <span className="mx-2 text-gray-500">or</span>
          <div className="border-t flex-grow border-gray-300"></div>
        </div>

        {/* Social Login */}
        <SocialLogin />  {/* Use the SocialLogin component here */}

        {/* Login Link */}
        <p className="text-center text-gray-500">
          Already have an account?{' '}
          <a href="/login" className="text-teal-600 underline hover:text-teal-500">Login</a>
        </p>
      </div>
    </div>
  );
};

export default SignIn;
