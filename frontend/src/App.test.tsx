import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import App from "./App";

describe("App", () => {
	it("render heading 1", () => {
		render(<App />);
		const headingElement = screen.getByRole("heading", { level: 1 });
		expect(headingElement).toBeInTheDocument();
	});
});
