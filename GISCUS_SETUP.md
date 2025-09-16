# Giscus Setup Instructions

Follow these steps to enable Giscus comments on your GitHub Pages site:

## Step 1: Enable GitHub Discussions
1. Go to https://github.com/JNK234/JNK234.github.io/settings
2. Scroll down to the "Features" section
3. Check the box next to "Discussions" to enable it
4. Click "Save"

## Step 2: Install the Giscus App
1. Visit https://github.com/apps/giscus
2. Click "Install"
3. Select your account "JNK234"
4. Choose "Only select repositories"
5. Select "JNK234.github.io"
6. Click "Install"

## Step 3: Create the Comments Category (if needed)
1. Go to https://github.com/JNK234/JNK234.github.io/discussions
2. Click on "Categories" (on the right side)
3. Check if a "Comments" category exists
4. If not, create a new category called "Comments"

## Step 4: Verify Configuration
Visit https://giscus.app and enter:
- Repository: `JNK234/JNK234.github.io`
- Discussion Category: `Comments`
- Page ↔️ Discussions Mapping: `Discussion title contains page title`

The configuration should match what's in your `_config.yml`:
```yaml
giscus:
  repo: JNK234/JNK234.github.io
  repo_id: R_kgDONgJNKA
  category: Comments
  category_id: DIC_kwDONgJNKM4CkxOo
  mapping: title
  strict: 1
  reactions_enabled: 1
  input_position: bottom
  dark_theme: dark
  light_theme: light
  emit_metadata: 0
  lang: en
```

## Step 5: Deploy and Test
1. Commit and push the changes to your repository
2. Wait for GitHub Pages to rebuild (usually 2-5 minutes)
3. Visit any blog post with `giscus_comments: true` in the front matter
4. The comments section should now appear at the bottom of the post

## Troubleshooting
- If comments don't appear, check the browser console for errors
- Ensure the repository is public
- Verify that Discussions are enabled in the repository settings
- Check that the Giscus app has access to your repository