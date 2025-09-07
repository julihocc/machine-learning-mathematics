# Copilot Instructions for Mathematics for Machine Learning Course

## Project Overview

This is an **open-source educational course** combining mathematics education with multi-modal content delivery (Jupyter notebooks + YouTube videos). The project follows a **dual-purpose design**: serving both professional learners and YouTube audiences.

**⚠️ AI Usage Policy**: This project follows strict guidelines for AI assistance. See [AI_MANIFESTO.md](../AI_MANIFESTO.md) for complete policies. Key points:
- All mathematical content must be human-verified for accuracy
- AI assists with organization and clarity, never replaces human expertise
- Transparency required for significant AI contributions
- Educational integrity and mathematical rigor are paramount

## Architecture & Key Components

### 📁 Content Structure
- **modules/**: 6 sequential mathematical modules (`01-foundations/` to `06-advanced-topics/`)
- **video-content/**: YouTube production materials (scripts/, slides/, assets/)
- **exercises/** & **solutions/**: Practice problems separate from main content
- **resources/**: Bibliography, datasets, supplementary materials

### 🔄 Multi-Modal Learning Pattern
Each module should contain:
- **theory notebooks**: Interactive mathematical explanations with code
- **examples notebooks**: Practical applications and worked problems
- **corresponding video scripts**: In `video-content/scripts/moduleXX/`
- **exercise sets**: Linked but separate practice materials

## Development Workflows

### Content Creation Process
1. **Start with notebooks**: Create mathematical content in Jupyter first
2. **Extract video scripts**: Adapt notebook content for video format
3. **Cross-link materials**: Ensure notebooks reference videos and vice versa
4. **Test mathematical accuracy**: Use `setup.py` to verify environment, then test all code

### Environment Setup
```bash
python setup.py  # Automated setup with dependency verification
# OR manual: pip install -r requirements.txt && jupyter lab
```

### Mathematical Content Standards
- **Progressive complexity**: Build from intuitive → rigorous → applied
- **Code-first approach**: Mathematical concepts demonstrated through Python
- **Consistent notation**: Use LaTeX in markdown cells, maintain notation across modules
- **Accessibility focus**: Clear explanations before formal definitions

## Project-Specific Conventions

### File Naming & Organization
- **Module naming**: `0X-module-name/` (zero-padded for ordering)
- **Notebook naming**: `theory.ipynb`, `examples.ipynb`, `exercises.ipynb`
- **Video scripts**: Mirror module structure in `video-content/scripts/`

### Python Stack Integration
- **Scientific computing core**: numpy, scipy, matplotlib, sympy
- **Educational tools**: jupyter, ipywidgets for interactive learning
- **Mathematical visualization**: Focus on clear, educational plots over complex graphics
- **Symbolic math**: Heavy use of SymPy for mathematical demonstrations

### Content Quality Patterns
- **Mathematical accuracy**: All equations must be verifiable and correct
- **Executable examples**: Every mathematical concept should have working code
- **Visual learning**: Plots and animations support mathematical intuition
- **Community-driven**: Content designed for collaboration and improvement

### YouTube Integration
- **Production workflow**: Scripts → slides → recording → linking back to notebooks
- **Accessibility requirements**: Captions, transcripts, clear visual design
- **Cross-platform consistency**: Maintain same notation and examples across mediums

## Key Dependencies & Integration Points

### Core Mathematical Libraries
- **SymPy**: Symbolic mathematics and LaTeX rendering
- **NumPy/SciPy**: Numerical computation and algorithms
- **Matplotlib/Seaborn**: Educational visualizations
- **Manim**: Mathematical animations (optional, for advanced visualizations)

### Educational Infrastructure
- **Jupyter ecosystem**: Interactive computing with widgets
- **Git-based collaboration**: Issues and discussions for community feedback
- **Creative Commons licensing**: Open educational resource principles

## Development Anti-Patterns to Avoid
- **Don't create generic tutorials**: Focus on ML-specific mathematical applications
- **Don't separate theory from practice**: Always combine mathematical concepts with code
- **Don't ignore accessibility**: Content must work for diverse learning needs
- **Don't break the learning sequence**: Modules build on each other deliberately

## Contributing Guidelines
- **Mathematical accuracy is paramount**: Verify all equations and code
- **Test notebooks completely**: Ensure all cells execute without errors
- **Follow the multi-modal pattern**: New content needs both notebook and video considerations
- **Maintain progressive difficulty**: New material should fit the learning sequence
