# Portfolio Projects Update Design
**Date:** October 27, 2025
**Objective:** Add NLP Interpretability project and refresh all existing projects with latest GitHub information using parallel multi-agent architecture

## Requirements

### Primary Goals
1. Add new project: NLP Interpretability (from local private repository)
2. Update all existing projects with latest GitHub information
3. Maintain existing project numbering and user customizations
4. Use parallel multi-agent architecture for maximum speed

### Constraints
- NLP repo is private, located at: `/Users/jnk789/Desktop/NW/FALL 2025/Independent Study/NLP-Independent-Study-`
- Must preserve existing project file numbers (1-7)
- Must maintain al-folio Jekyll theme formatting
- Category for NLP project: "research"
- No automatic git commits (user reviews first)

### Source Repositories
Public GitHub repos (from jnk-info/repositorys_project_info.md):
1. https://github.com/JNK234/Agentic-Blogging-Assistant
2. https://github.com/can-gurkan/LEAR.git
3. https://github.com/JNK234/AdVocate-Agentic-Ad-Generator.git
4. https://github.com/JNK234/Second-OpinAIon.git
5. https://github.com/JNK234/FaceSwap-Diffusion-Model.git
6. https://github.com/JNK234/Netlogo-LLM-Extension.git

Local repo:
7. /Users/jnk789/Desktop/NW/FALL 2025/Independent Study/NLP-Independent-Study-

## Architecture Overview

### Parallel Multi-Agent System

**Agent Composition:**
- **6 GitHub Repository Analyzer Agents** - One per public repository
- **1 Local Repository Analyzer Agent** - For private NLP project
- **1 Consolidator Agent** - Coordinates results and updates project files

**Total Agents Deployed:** 8 agents (7 analyzers + 1 consolidator)

### Agent Responsibilities

#### Repository Analyzer Agents (GitHub)
Each agent independently:
1. Fetches repository data from GitHub
2. Extracts README content, tech stack, key features
3. Analyzes recent commits and project activity
4. Generates structured project metadata
5. Returns standardized JSON to consolidator

#### Repository Analyzer Agent (Local - NLP Project)
Performs local analysis:
1. Reads README.md and documentation files
2. Scans code structure to identify tech stack
3. Examines requirements.txt, package.json, or similar
4. Analyzes Python/Jupyter notebooks for project scope
5. Extracts research objectives and findings
6. Returns same standardized JSON structure

#### Consolidator Agent
Final coordination:
1. Waits for all 7 analyzer agents to complete
2. Maps fetched data to existing project files
3. Creates new project file for NLP Interpretability (8_project.md)
4. Updates existing projects with fresh GitHub data
5. Preserves user customizations (images, manual descriptions)
6. Ensures consistent al-folio formatting

## Data Flow

### Phase 1: Parallel Repository Analysis

**Execution Model:** All 7 analyzer agents launch simultaneously

**Standardized Output Schema:**
```json
{
  "repo_url": "https://github.com/..." or "local",
  "repo_name": "Project Name",
  "description": "Brief project description",
  "detailed_features": ["Feature 1", "Feature 2"],
  "tech_stack": ["Python", "FastAPI", "React"],
  "category": "research|work|fun",
  "importance": 1-7,
  "key_achievements": "Notable results/impact",
  "existing_project_file": "2_project.md" or null
}
```

### Phase 2: Consolidation & File Updates

**Consolidator Workflow:**

1. **Map Results to Existing Files**
   - Match GitHub URLs to current project files (_projects/1_project.md through 7_project.md)
   - Use GitHub URL as primary identifier
   - Preserve existing file numbering

2. **Assign New Project Number**
   - NLP Interpretability → 8_project.md
   - Importance field controls display order (independent of filename)

3. **Preserve User Customizations**
   - Keep manually added images (`img:` field)
   - Retain custom descriptions if significantly different from README
   - Maintain any special formatting

4. **Update Fresh Data**
   - Refresh tech stacks from current repo state
   - Update features based on latest README
   - Sync GitHub links

5. **Maintain al-folio Formatting**
   - Proper YAML frontmatter
   - Category validation (work, research, fun)
   - Markdown structure consistency

### File Naming Strategy
- **Existing projects:** Keep numbers 1-7
- **New NLP project:** Assigned number 8
- **Display order:** Controlled by `importance:` field in frontmatter
- **Categories:** Groups projects on page (work, research, fun)

## Error Handling & Quality Assurance

### Agent Failure Resilience

**Isolation Strategy:**
- Each agent operates independently
- One agent failure doesn't affect others
- Consolidator proceeds with available data
- Failed repos logged with specific error details
- User notified of any failures with repo names

### Data Quality Checks

**Pre-Update Validation:**
1. **GitHub URL Accessibility** - Verify public repos are accessible
2. **Local Path Verification** - Confirm NLP repo path exists
3. **Content Completeness** - Ensure minimum required fields present
4. **Markdown Syntax** - Validate proper frontmatter structure
5. **Image References** - Preserve existing `img:` fields
6. **Category Validity** - Ensure categories match allowed values

### Rollback Safety

**Protection Mechanisms:**
1. Backup existing project files before modification
2. Changes staged but not auto-committed
3. User reviews git diff before commit
4. Clear summary of what was added/updated

### Special Handling: Private NLP Repository

**Considerations:**
- No GitHub URL in project file (or placeholder for future)
- Focus on research contributions and technical approach
- Highlight academic/interpretability aspects
- Emphasize methodology and findings

## Implementation Strategy

### Execution Phases

**Phase 1: Launch Parallel Analyzers**
- Deploy all 7 analyzer agents simultaneously
- Each agent receives: repo URL (or local path), agent instructions
- Agents use Explore subagent_type for GitHub repos
- Local analyzer uses Read + Grep for file analysis

**Phase 2: Aggregate Results**
- Consolidator collects all 7 JSON outputs
- Validates data completeness
- Reports any failed analyzers

**Phase 3: Update Project Files**
- Map results to existing files
- Create 8_project.md for NLP Interpretability
- Update content while preserving structure
- Generate summary of changes

**Phase 4: User Review**
- Present git diff to user
- Summarize what was added/updated
- Await user approval for commit

## Success Criteria

### Functional Requirements
- ✓ All 7 repositories analyzed successfully
- ✓ NLP Interpretability project created as 8_project.md
- ✓ Existing projects updated with latest information
- ✓ No duplicate content or broken links
- ✓ Proper al-folio formatting maintained

### Performance Requirements
- ✓ Analysis completes faster than sequential approach
- ✓ All agents execute in parallel (not sequential)
- ✓ Failed agents don't block overall progress

### Quality Requirements
- ✓ User customizations preserved
- ✓ Consistent markdown formatting
- ✓ Valid category assignments
- ✓ Accurate tech stack information
- ✓ Clear project descriptions

## Risk Mitigation

### Identified Risks

1. **Risk:** GitHub API rate limiting
   **Mitigation:** Use Explore agent with built-in retry logic; stagger requests slightly

2. **Risk:** Local NLP repo path inaccessible
   **Mitigation:** Verify path exists before deployment; fail fast with clear error

3. **Risk:** Conflicting updates to same project file
   **Mitigation:** Single consolidator handles all updates; no concurrent writes

4. **Risk:** Loss of user customizations
   **Mitigation:** Preserve existing img fields, validate before overwrite

5. **Risk:** Invalid category assignments
   **Mitigation:** Category validation against allowed values (work, research, fun)

## Next Steps

1. **Worktree Setup** (Optional - if isolating work)
2. **Implementation Planning** - Detailed task breakdown
3. **Parallel Agent Deployment** - Execute Phase 1
4. **Consolidation** - Execute Phase 2-3
5. **User Review & Commit** - Execute Phase 4
