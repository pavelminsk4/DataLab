def fill_social_part_of_sample(p):
  return f'''
    <section class="email-post-wrapper">
      <h2 class="email-post-title">
        {p.user_name}
      </h2>
      <p class="email-post-content">
        {p.text}
      </p>
      </div>
      <a href="https://twitter.com/{p.user_alias}/status/{p.post_id}" class="email-post-button">
        View Post
      </a>
    </section>
  '''
