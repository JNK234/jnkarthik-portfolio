---
layout: cv
permalink: /cv/
title: cv
nav: true
nav_order: 4
cv_pdf: Narasimha_Karthik_Resume.pdf
description: My comprehensive curriculum vitae highlighting my experience in AI/ML, research work, and technical achievements.
---

<!-- PDF Download Section -->
<div class="alert alert-info" role="alert">
  <div class="d-flex align-items-center justify-content-between flex-wrap">
    <div class="mb-2 mb-md-0">
      <i class="fa-solid fa-info-circle me-2"></i>
      <strong>Multiple Formats Available:</strong> View my CV in structured web format below, or download the traditional PDF version.
    </div>
    <div class="btn-group" role="group" aria-label="CV Download Options">
      <a href="{{ 'assets/pdf/' | append: page.cv_pdf | relative_url }}" class="btn btn-primary" target="_blank">
        <i class="fa-solid fa-download me-1"></i> Download PDF
      </a>
      <a href="{{ 'assets/pdf/' | append: page.cv_pdf | relative_url }}" class="btn btn-outline-primary" target="_blank">
        <i class="fa-solid fa-external-link me-1"></i> View PDF
      </a>
    </div>
  </div>
</div>

<!-- Web Version Introduction -->
<div class="mb-4">
  <p class="lead">This interactive web version of my CV provides detailed information about my experience, skills, and achievements in AI/ML and data science.</p>
</div>

<!-- Structured CV Content will be automatically rendered by the cv layout -->
