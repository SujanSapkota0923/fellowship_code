import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: '/fellowship_code/frontend/',
  plugins: [react()],
})

// config to export repo on github pages
