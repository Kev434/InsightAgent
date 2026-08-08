/**
 * Root Layout
 *
 * TODO:
 * - Import global CSS (globals.css with Tailwind directives)
 * - Set metadata (title: "InsightAgent", description: "...")
 * - Add a consistent layout wrapper (header, sidebar, main content area)
 * - Wrap children with AuthProvider context (for login state)
 */

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "InsightAgent",
  description: "AI-powered financial data insights platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // TODO: Add global styles, auth provider, layout structure
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
