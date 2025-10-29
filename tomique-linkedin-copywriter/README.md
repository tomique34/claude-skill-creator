# Tomique LinkedIn Copywriter Skill

Personalized Claude Agent Skill for creating engaging LinkedIn posts in Tomáš Vince's authentic writing style. Transforms article URLs, personal experiences, and technical insights into professional, human-sounding LinkedIn content in Slovak or English.

## What This Skill Does

Creates LinkedIn posts that:
- **Sound authentically human** - No AI-tell phrases or robotic language
- **Match your voice** - Writes in Tomáš Vince's specific style and tone
- **Encourage engagement** - Includes hooks, insights, and discussion-worthy CTAs
- **Are ready to publish** - Proper formatting, hashtags, under 1000 characters
- **Work in both languages** - Slovak and English supported

## Features

### Four Post Types Supported

1. **Article Commentary** - Transform article URLs into thoughtful posts with your perspective
2. **Personal Experience** - Turn project stories and lessons into engaging narratives
3. **Technical Insights** - Share practical tips, tools, and architectural wisdom
4. **Industry Trends** - Comment on tech trends with your unique angle

### Both Languages

- **Slovak** - Personal, direct, motivational tone
- **English** - Professional yet approachable, global perspective

### URL Support

- **Automatic** - Fetches article content from URL
- **Manual** - Paste article text if automatic fetch fails
- **Flexible** - Works with or without source material

### Quality Guarantees

✅ Under 1000 characters
✅ Strategic emojis (2-4)
✅ Exactly 6 relevant hashtags
✅ Compelling hook
✅ Engagement-worthy CTA
✅ No AI-tell phrases
✅ Authentic voice

## Installation

### Option 1: Global Installation

```bash
# Create global skills directory
mkdir -p ~/.claude/skills

# Copy the skill
cp -r tomique-linkedin-copywriter ~/.claude/skills/
```

### Option 2: Project-Specific Installation

```bash
# From your project root
mkdir -p .claude/skills
cp -r tomique-linkedin-copywriter .claude/skills/
```

## Usage

Once installed, Claude Code will automatically use this skill when you request LinkedIn content creation.

### Basic Commands

**Slovak Posts:**
```
"Vytvor LinkedIn post v slovenčine o tomto článku: [URL]"
"Napíš post o mojej skúsenosti s [téma] po slovensky"
"Vytvor technický tip o Cloud automation v slovenčine"
```

**English Posts:**
```
"Create LinkedIn post about this article: [URL]"
"Write post about my experience with [topic]"
"Generate technical insight about Kubernetes optimization"
```

### Specify Post Type

**Article Commentary:**
```
"Create article commentary post from [URL] in English"
"Komentár na článok [URL] po slovensky"
```

**Personal Experience:**
```
"Write personal experience post about [project/situation]"
"Post o mojej skúsenosti s [projekt] v slovenčine"
```

**Technical Insight:**
```
"Technical insight post about [topic] in English"
"Technický tip o [téma] po slovensky"
```

**Industry Trend:**
```
"Industry trend commentary on [trend] in English"
"Komentár k trendu [téma] v slovenčine"
```

### With URL Articles

**Automatic Fetch:**
```
"Generate LinkedIn post from this article [URL] in Slovak"
→ Skill will fetch article content automatically
```

**Manual Content:**
```
"Create post about this article in English:

[Paste article text]
"
→ Works if automatic fetch fails
```

### Specify Requirements

```
"Create Slovak post about AI agents. Focus on practical implementation. Technical audience."

"Write English post on cloud costs. Include specific numbers. Keep it under 800 characters."
```

## What the Skill Will Do

### 1. Language Selection
Confirms Slovak or English based on your request

### 2. Post Type Identification
Determines which template to use (article, experience, insight, trend)

### 3. Content Analysis
- Fetches or analyzes source material
- Identifies key points and insights
- Finds your unique angle

### 4. Post Creation
- Crafts compelling hook
- Builds story or insight body
- Adds specific examples and numbers
- Creates engagement-worthy CTA

### 5. Formatting
- Strategic emojis (2-4)
- Bold for emphasis
- Short paragraphs
- Mobile-friendly layout

### 6. Hashtags
- Exactly 6 hashtags
- Mix of broad and specific
- At least 1 technology-specific
- Relevant to content

### 7. Quality Check
- Under 1000 characters
- No AI-tell phrases
- Sounds like Tomáš Vince
- Ready to copy-paste

## Output Example

**Request:**
```
"Create Slovak post about my experience with AI agent that failed in production"
```

**Output:**
```
Nasadili sme AI agenta do produkcie. Po 2 dňoch ho klient vypol. 🤔

Prečo?

Agent mal 95% accuracy.
Bol 10x rýchlejší než človek.
Šetril 20 hodín týždenne.

Problém?
Nikto mu neveril.

Zistili sme:
→ AI zvládal bežné situácie perfektne
→ Ale edge cases (20% práce) potrebovali človeka
→ Nebol jasný handoff medzi AI a human
→ Ľudia cítili stratu kontroly

Čo sme zmenili:
1. AI navrhuje, človek potvrdzuje
2. Clear confidence score pri každom rozhodnutí
3. Easy override mechanizmus
4. Postupné zvyšovanie automatizácie

Výsledok:
Používajú to denne.
Začali sme na 30% automatizácie.
Mesiac 3: Už na 75%.
Team to miluje.

Lesson learned:
Neautomatizuj procesy.
Augmentuj ľudí.

Aké sú vaše skúsenosti s AI adoption? Čo fungovalo?

#AI #Automation #ChangeManagement #ProductDevelopment #TechLeadership #UserExperience
```

## Skill Structure

```
tomique-linkedin-copywriter/
├── SKILL.md                          # Main skill instructions
├── README.md                         # This file
├── templates/
│   ├── ARTICLE_COMMENTARY_TEMPLATE.md
│   ├── PERSONAL_EXPERIENCE_TEMPLATE.md
│   ├── TECHNICAL_INSIGHT_TEMPLATE.md
│   └── INDUSTRY_TRENDS_TEMPLATE.md
├── reference/
│   ├── WRITING_STYLE_GUIDE.md        # Tomáš's style analysis
│   ├── AI_PHRASES_TO_AVOID.md        # AI-tell signs list
│   └── HASHTAG_LIBRARY.md            # Curated hashtags
└── examples/
    ├── personal-experience-slovak.md
    └── technical-insight-english.md
```

## Tips for Best Results

### Be Specific

**Vague:**
```
"Create post about cloud"
```

**Better:**
```
"Create English post about cloud cost optimization. Focus on data transfer costs. Include specific AWS example."
```

### Provide Context

**Basic:**
```
"Write post about my project"
```

**Better:**
```
"Write Slovak post about migrating 50 microservices to Kubernetes. It took 3 months, saved 40% costs, zero downtime. Lesson: start small, validate, then scale."
```

### Specify Audience

```
"Technical insight for Cloud Architects about Terraform state management"
"Personal story for general tech audience about team collaboration"
```

### Request Iterations

```
"Make it more technical"
"Add more specific numbers"
"Make the hook more provocative"
"Shorten to under 700 characters"
```

## Common Use Cases

### Morning Routine

```
"I read this article [URL]. Create Slovak LinkedIn post with my commentary."
```

### After Project Success

```
"Just finished cloud migration for [client]. Saved them 45% on costs. Write English post about lessons learned."
```

### Sharing Technical Tips

```
"Create English post: Kubernetes memory optimization tip. Most teams miss resource limits on init containers. Show impact."
```

### Trend Commentary

```
"Everyone's talking about AI agents. Write Slovak post with realistic perspective from my production experience."
```

## Validation

To validate the skill structure:

```bash
python3 claude-skill-creator/scripts/validate_skill.py tomique-linkedin-copywriter
```

## Customization

### Add Your Posts

Add your own LinkedIn posts to `examples/` directory for reference:

```bash
# Create new example file
cat > tomique-linkedin-copywriter/examples/my-post-example.md << 'EOF'
[Your actual LinkedIn post that performed well]
EOF
```

The skill will learn from your examples.

### Update Style Guide

Edit `reference/WRITING_STYLE_GUIDE.md` based on your evolving voice and preferences.

## Troubleshooting

### Post Sounds Too AI-Like

**Issue**: Generated post uses AI phrases or sounds robotic

**Solution**:
```
"Rewrite this without AI phrases. Make it sound more conversational."
"This sounds too corporate. Make it more personal and direct."
```

### Wrong Language

**Issue**: Generated in English when you wanted Slovak

**Solution**: Explicitly specify language in request
```
"V slovenčine vytvor..." or "Create in Slovak..."
```

### Too Long

**Issue**: Post exceeds 1000 characters

**Solution**:
```
"Shorten to under 800 characters"
"Keep only the most important points"
```

### Missing Technical Depth

**Issue**: Too general, not specific enough

**Solution**:
```
"Add more technical details"
"Include specific tools and commands"
"Show the actual implementation"
```

### Wrong Tone

**Issue**: Too formal or too casual

**Solution**:
```
"Make it more conversational"
"Professional but approachable tone"
"Write it like explaining to a colleague over coffee"
```

## Best Practices

### For Article Posts

1. Read the article first
2. Decide your angle (agree/disagree/expand)
3. Connect to your real experience
4. Add practical takeaway

### For Experience Posts

1. Start with specific situation
2. Include real numbers
3. Show the challenge and solution
4. Extract universal lesson

### For Technical Posts

1. Lead with the problem
2. Explain why current approach fails
3. Show your solution with steps
4. Include real results

### For Trend Posts

1. Take a clear stance
2. Support with your observations
3. Show nuance
4. Make actionable prediction

## Requirements

- Claude Code (claude.ai/code)
- This skill placed in `.claude/skills/` or `~/.claude/skills/`
- (Optional) WebFetch capability for automatic URL content fetching

## About

Created for **Tomáš Vince** - Cloud Architect, IoT specialist, and AI automation enthusiast.

**LinkedIn**: https://linkedin.com/in/tomasvince

**Focus Areas**:
- Cloud Architecture (AWS, Azure, GCP)
- IoT & Edge Computing
- AI Agents & Automation
- No-Code/Low-Code Tools
- Productivity Enhancement

## License

Personal use skill for Tomáš Vince. Part of claude-skill-creator collection.

## Support

For issues or improvements, update the SKILL.md or reference materials based on your evolving needs and voice.
