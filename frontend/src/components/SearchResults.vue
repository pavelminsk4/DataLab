<template>
  <div class="search-result-wrapper">
    <div class="filters">Filters</div>
    <div v-if="searchData.length" class="search-result-cards">
      <div
        v-for="(item, index) in searchData"
        :key="'result' + index"
        class="search-result-card"
      >
        <div>Checkbox</div>

        <section class="search-info-wrapper">
          <div class="result-img">
            <img :src="item.entry_media_thumbnail_url" class="img" />
          </div>
          <div class="search-info">
            <div class="title" tabindex="0">{{ item.entry_title }}</div>
            <div class="description" tabindex="0">{{ item.entry_summary }}</div>
            <div class="general-information">
              <div>
                {{ resultLanguage(item.feed_language) }}
              </div>
              <div>
                {{ item.entry_published }}
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div v-else>No results.</div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import {langCodes} from '@/lib/language-codes'

export default {
  name: 'SearchResults',
  computed: {
    ...mapState(['searchData']),
  },
  methods: {
    resultLanguage(langCode) {
      for (let key in langCodes) {
        if (key === langCode) {
          return langCodes[key]
        }
      }
      return ''
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  max-width: 50%;
  margin-left: 108px;

  color: var(--primary-text-color);
}

.filters {
  margin-bottom: 25px;
}

.search-result-cards {
  max-width: 100%;
}

.search-result-card {
  max-width: 100%;

  margin-bottom: 10px;
  padding: 12px 21px 17px 20px;

  background: var(--secondary-bg-color);
  border-radius: 10px;
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
}

.search-info-wrapper {
  display: flex;
}

.result-img {
  width: 71px;
  height: 71px;
  margin-right: 18px;

  .img {
    width: inherit;
  }
}

.search-info {
  display: flex;
  flex-direction: column;

  overflow: hidden;

  .title {
    cursor: pointer;

    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;

    margin-bottom: 10px;

    font-weight: 600;
    font-size: 16px;
    line-height: 22px;
  }

  .title:focus {
    white-space: normal;
  }

  .description {
    cursor: pointer;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;

    font-weight: 400;
    font-size: 14px;
    line-height: 150%;
  }

  .description:focus {
    -webkit-box-orient: revert;
  }
}

.general-information {
  display: flex;
}
</style>
