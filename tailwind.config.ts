extend: {
  borderRadius: {
    lg: "var(--radius)",
    md: "calc(var(--radius) - 2px)",
    sm: "calc(var(--radius) - 4px)",
  },
  boxShadow: {
    'card': 'var(--shadow-card)',
    'emergency': 'var(--shadow-emergency)',
    'glow': 'var(--shadow-glow)',
  },
  keyframes: {
    "accordion-down": {
      from: { height: "0" },
      to: { height: "var(--radix-accordion-content-height)" },
    },
    "accordion-up": {
      from: { height: "var(--radix-accordion-content-height)" },
      to: { height: "0" },
    },
    "fade-in": {
      "0%": { opacity: "0", transform: "translateY(20px)" },
      "100%": { opacity: "1", transform: "translateY(0)" },
    },
    "bounce-in": {
      "0%": { transform: "scale(0.8)", opacity: "0" },
      "50%": { transform: "scale(1.05)" },
      "100%": { transform: "scale(1)", opacity: "1" },
    },
    "pulse-glow": {
      "0%, 100%": { opacity: "1" },
      "50%": { opacity: "0.7" },
    },
  },
  animation: {
    "accordion-down": "accordion-down 0.2s ease-out",
    "accordion-up": "accordion-up 0.2s ease-out",
    "fade-in": "fade-in 0.6s ease-out",
    "bounce-in": "bounce-in 0.5s ease-out",
    "pulse-glow": "pulse-glow 2s ease-in-out infinite",
  },
}
