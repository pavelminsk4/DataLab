<template>
  <div class="search-result-wrapper">
    <div class="filters">
      <div>{{ searchData.length }} results</div>

      <div class="calendar-wrapper">
        <div class="trigger-wrapper" @click="openCalendar">
          <CalendarIcon class="dp-icon" />
          <div>{{ calendarDate }}</div>
          <ArrowDownIcon :class="[isShowCalendar && 'open-calendar']" />
        </div>
        <BaseCalendar v-if="isShowCalendar" />
      </div>
    </div>
    <div v-if="loading" class="spinner-wrapper"><BaseSpinner /></div>
    <div v-if="searchData.length" class="search-result-cards">
      <div
        v-for="(item, index) in searchData"
        :key="'result' + index"
        class="search-result-card"
      >
        <section class="search-info-wrapper">
          <div class="result-img">
            <BaseCheckbox class="status-checkbox" />
            <img
              v-if="item.entry_media_thumbnail_url !== 'None'"
              :src="item.entry_media_thumbnail_url"
              class="img"
            />
            <NoImageIcon v-else class="default-image" />
          </div>

          <div class="search-info">
            <div
              :class="[
                item.sentiment === 'positive' && 'status-positive',
                item.sentiment === 'negative' && 'status-negative',
                'status-default',
              ]"
            >
              {{ capitalizeFirstLetter(item.sentiment) }}
            </div>
            <div class="title" tabindex="0">{{ item.entry_title }}</div>
            <div class="description" tabindex="0">{{ item.entry_summary }}</div>
            <div class="general-information">
              <div class="general-item">
                {{ item.feedlink__source1 }}
              </div>
              <div class="general-item">
                {{ item.feedlink__country }}
              </div>
              <div class="general-item">
                {{ item.feed_language__language }}
              </div>
              <div class="general-item">
                {{ dateOfCreation(item.entry_published) }}
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div v-if="!loading">No results.</div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'

import BaseSpinner from '@/components/BaseSpinner'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseCalendar from '@/components/datepicker/BaseCalendar'

import NoImageIcon from '@/components/icons/NoImageIcon'
import CalendarIcon from '@/components/icons/CalendarIcon'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import {action} from '@store/constants'

export default {
  name: 'SearchResults',
  components: {
    ArrowDownIcon,
    CalendarIcon,
    BaseCalendar,
    BaseCheckbox,
    BaseSpinner,
    NoImageIcon,
  },
  data() {
    return {
      isShow: false,
    }
  },
  created() {
    document.addEventListener('click', this.close)
  },
  computed: {
    ...mapState([
      'searchData',
      'loading',
      'additionalFilters',
      'isShowCalendar',
    ]),
    calendarDate() {
      if (this.additionalFilters?.date_range?.length) {
        const currentDate = this.additionalFilters?.date_range.map((el) =>
          this.formatDate(el)
        )

        return `${currentDate[0]} - ${currentDate[1]}`
      } else {
        return `${this.formatDate(this.getLastWeeksDate())} - ${this.formatDate(
          new Date()
        )}`
      }
    },
  },
  methods: {
    ...mapActions([action.REFRESH_DISPLAY_CALENDAR]),
    dateOfCreation(date) {
      return new Date(date).toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
      })
    },
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1)
    },
    formatDate(date) {
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    openCalendar() {
      if (this.isShowCalendar) {
        this.isShow = false
      } else {
        this.isShow = true
      }
      this[action.REFRESH_DISPLAY_CALENDAR](this.isShow)
    },
    close() {
      const elements = document.querySelectorAll('.calendar-wrapper')

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this[action.REFRESH_DISPLAY_CALENDAR](false)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 43vw;

  color: var(--primary-text-color);
}

.trigger-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  max-width: 270px;
  padding: 10px 16px 10px 25px;

  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 8px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-text-color);

  cursor: pointer;
}

.open-calendar {
  transform: rotate(180deg);
}

.filters {
  display: flex;
  align-items: center;
  justify-content: space-between;

  width: 100%;
  margin-bottom: 25px;

  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--secondary-text-color);
}

.spinner-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  min-width: 100%;
  margin-bottom: 80px;
}

.search-result-cards {
  overflow: auto;

  height: 1000px;
  width: 100%;

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 10px;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}

.search-result-card {
  max-width: 100%;

  margin: 0 10px 10px 0;
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

.status-checkbox {
  color: var(--secondary-text-color);

  margin-bottom: 12px;
}

.status-default {
  position: relative;

  color: var(--secondary-text-color);

  padding-left: 12px;
  margin-bottom: 12px;

  &:before {
    position: absolute;
    top: 50%;
    left: 4px;
    transform: translate(-50%, -50%);

    content: '';
    width: 6px;
    height: 6px;

    border-radius: 100%;
    background-color: var(--secondary-text-color);
  }
}

.status-positive {
  color: var(--tag-color);

  &:before {
    background-color: var(--tag-color);
  }
}

.status-negative {
  color: var(--negative-status);

  &:before {
    background-color: var(--negative-status);
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

  margin-top: 10px;

  .general-item {
    position: relative;

    margin-right: 20px;

    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
    color: var(--secondary-text-color);

    &:not(:last-child):before {
      position: absolute;
      top: 50%;
      right: -13px;
      transform: translate(-50%, -50%);

      content: '';

      width: 4px;
      height: 4px;

      border-radius: 100%;
      background-color: var(--secondary-text-color);
    }
  }
}

.default-image {
  width: 71px;
  height: 50px;
}

@media screen and (max-width: 1000px) {
  .search-result-wrapper {
    align-items: flex-end;
  }

  .filters {
    align-items: flex-end;
    flex-direction: column;
  }

  .search-result-card {
    margin: 0 0 10px 0;
  }
}
</style>
