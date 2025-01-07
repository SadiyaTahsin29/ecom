import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders navigation links", () => {
  render(<App />);
  const homeLink = screen.getByText(/Home/i);
  const newArrivalsLink = screen.getByText(/New Arrivals/i);
  expect(homeLink).toBeInTheDocument();
  expect(newArrivalsLink).toBeInTheDocument();
});
