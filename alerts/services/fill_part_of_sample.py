from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

def fill_part_of_sample(p):
  return f'''
    <section class="email-post-wrapper">
      <div class="email-post-date">{str(p.entry_published.ctime())}</div>
      <h2 class="email-post-title">
        {p.entry_title}
      </h2>
      <p class="email-post-content">
        {p.entry_summary}
      </p>
      <div class="email-post-info">
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/language.png" />
          <span>Language: {p.feed_language.language}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/sentiment.png" />
          <span>Sentiment: {p.sentiment}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/source.png" />
          <span>Source: {p.feedlink.source1}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/location.png" />
          <span>Source country: {p.feedlink.country}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/global-rank.png" />
          <span>Global Rank: {p.feedlink.alexaglobalrank}</span>
        </div>
        <div class="email-post-info-item">
          <img src="{env('APP_URL')}/static/email_alerts_icons/calendar.png" />
          <span>Date: {str(p.entry_published.ctime())}</span>
        </div>
      </div>
      <a href="{p.entry_links_href}" class="email-post-button">
        View Post
      </a>
    </section>
  '''
