document.addEventListener('DOMContentLoaded', () => {
    // Define the photos folder
    const photosFolder = 'photos/';
    const gallery = document.getElementById('gallery');

    // Folders representing excursions
    const excursions = [
        'excursion-1',
        'excursion-2',
        'excursion-3',
        // Add new folder names here for more excursions
    ];

    // Dynamically populate gallery
    excursions.forEach((excursion) => {
        // Create a column for each excursion
        const col = document.createElement('div');
        col.className = 'col-md-4';

        // Create a card for each excursion
        const card = `
            <div class="card mb-4">
                <img src="${photosFolder}${excursion}/photo1.jpg" class="card-img-top" alt="${excursion}">
                <div class="card-body">
                    <h5 class="card-title">${excursion.replace('-', ' ').toUpperCase()}</h5>
                    <a href="${photosFolder}${excursion}/index.html" class="btn btn-primary">View Photos</a>
                </div>
            </div>
        `;

        col.innerHTML = card;
        gallery.appendChild(col);
    });
});
