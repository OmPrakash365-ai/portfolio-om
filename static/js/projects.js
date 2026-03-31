const projectSearchForm = document.getElementById('project-search-form');
const projectSearchInput = document.getElementById('project-search');
const techSearchInput = document.getElementById('tech-search');
const projectCards = Array.from(document.querySelectorAll('.grid .card'));
const filterProjects = () => {
  const titleQuery = (projectSearchInput?.value || '').trim().toLowerCase();
  const techQuery = (techSearchInput?.value || '').trim().toLowerCase();
  projectCards.forEach((card) => {
    const title = (card.querySelector('h3')?.textContent || '').toLowerCase();
    const tech = Array.from(card.querySelectorAll('.tech-badge'))
      .map((badge) => badge.textContent.toLowerCase())
      .join(' ');
    const matchesTitle = !titleQuery || title.includes(titleQuery);
    const matchesTech = !techQuery || tech.includes(techQuery);
    card.style.display = matchesTitle && matchesTech ? '' : 'none';
  });
};
if (projectSearchForm) {
  projectSearchForm.addEventListener('submit', (event) => {
    event.preventDefault();
    filterProjects();
  });
}
projectSearchInput?.addEventListener('input', filterProjects);
techSearchInput?.addEventListener('input', filterProjects);
