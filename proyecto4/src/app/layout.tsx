import { Analytics } from '@vercel/analytics/react'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: "Dijkstra's Algorithm Visualizer - by Lara Solutions",
  description: "A graph visualization tool that can simulate Dijkstra's shortest path algorithm.",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <head>
      <link rel="icon" href="public/favicon.ico" />
      </head>
      <body>{children}</body>
    </html>
  );
}
