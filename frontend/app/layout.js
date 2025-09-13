// app/layout.js
import './globals.css';

// ... rest of your layout code
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}