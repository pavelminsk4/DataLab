<template>
  <div class="search-result-wrapper">
    <div class="filters">
      <div v-if="isCheckboxClippingWidget" class="clipping-wrapper">
        <BaseCheckbox />
        <ArrowDownIcon
          @click="openClippingDropdown"
          :class="['icon', isOpenClippingDropdown && 'icon-flip']"
        />

        <div v-if="isOpenClippingDropdown" class="dropdown">
          <div class="item" @click="createClippingWidget">
            <ClippingIcon /> Clipping
          </div>
        </div>
      </div>

      <div v-if="isShowSortingField" class="sorting-wrapper">
        Sort by
        <BaseSelect
          v-model="sortingValueProxy"
          :list="sortingList"
          @select-option="selectItem"
          name="aggregation-period"
          class="sorting-select"
        />
      </div>

      <div class="search-results">{{ numberOfPosts }} results</div>

      <div v-if="isShowCalendar" class="calendar-wrapper">
        <div class="trigger-wrapper" @click="openCalendar">
          <CalendarIcon class="dp-icon" />
          <div>{{ calendarDate }}</div>
          <ArrowDownIcon :class="[isShowCalendarContents && 'open-calendar']" />
        </div>
        <BaseCalendar
          v-if="isShowCalendarContents"
          :current-project="currentProject"
        />
      </div>
    </div>
    <div v-if="loading && searchLoading" class="spinner-wrapper">
      <BaseSpinner />
    </div>

    <div v-if="searchData.length" class="search-result-cards scroll">
      <BaseClippingCard
        v-for="(item, index) in searchData"
        :key="'result' + index"
        :img="cardImg(item)"
        :sentiment="item.sentiment"
        :title="item.entry_title"
        :entry-link="item.entry_links_href"
        :source-link="item.feedlink__sourceurl"
        :summary="item.entry_summary"
        :source="item.feedlink__source1"
        :country="item.feedlink__country"
        :language="item.feed_language__language"
        :potential-reach="item.feedlink__alexaglobalrank"
        :published="item.entry_published"
        :id="item.id"
        :is-checkbox-clipping-widget="isCheckboxClippingWidget"
        :clipping-element="selectedClippingElement(item.id)"
        :current-project="currentProject"
        @add-element="onChange"
      />
    </div>
    <div v-if="searchData.length" class="pagination-wrapper">
      <section class="dropdown-wrapper">
        <div @click="openDropdown">
          {{ countPosts }}
          <ArrowDownIcon
            :class="[isOpenDropdown && 'arrow-open-dropdown', 'arrow-down']"
          />
        </div>

        <div v-if="isOpenDropdown" class="dropdown">
          <div
            v-for="(item, index) in postsOnPage"
            :key="'drop' + index"
            class="item"
            @click="updatePostsCount(item)"
          >
            {{ item }}
          </div>
        </div>
      </section>
      <VPagination
        v-model="page"
        :pages="this.numberOfPages"
        :range-size="1"
        active-color="#055FFC"
        :container-class="'pagination'"
        :page-class="'page-item'"
        @update:modelValue="pageChangeHandler"
      />
    </div>
    <div v-if="!loading && !searchData.length && searchLoading">
      No results.
    </div>
  </div>
</template>

<script>
import VPagination from '@hennge/vue3-pagination'
import '@hennge/vue3-pagination/dist/vue3-pagination.css'

import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import BaseSpinner from '@/components/BaseSpinner'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseCalendar from '@/components/datepicker/BaseCalendar'
import BaseClippingCard from '@/components/BaseClippingCard'

import CalendarIcon from '@/components/icons/CalendarIcon'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import ClippingIcon from '@/components/icons/ClippingIcon'
import BaseSelect from '@/components/BaseSelect'

export default {
  name: 'SearchResults',
  components: {
    BaseSelect,
    ClippingIcon,
    BaseCheckbox,
    BaseClippingCard,
    ArrowDownIcon,
    CalendarIcon,
    BaseCalendar,
    BaseSpinner,
    VPagination,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
    isCheckboxClippingWidget: {
      type: Boolean,
      default: false,
    },
    clippingContent: {
      type: [Array, Object],
      default: () => [],
    },
    isShowCalendar: {
      type: Boolean,
      default: true,
    },
    searchLoading: {
      type: Boolean,
      default: false,
    },
    isShowSortingField: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['update-page', 'update-posts-count'],
  data() {
    return {
      isShow: false,
      isOpenClippingDropdown: false,
      clippingElements: [],
      isOpenDropdown: false,
      page: 1,
      countPosts: 20,
      postsOnPage: [20, 50, 100],
      sortingValue: '',
    }
  },
  computed: {
    ...mapState([
      'searchData',
      'loading',
      'additionalFilters',
      'isShowCalendarContents',
      'numberOfPages',
      'numberOfPosts',
    ]),
    sortingValueProxy: {
      get() {
        return this.sortingValue
      },
      set(value) {
        this.sortingValue = value
      },
    },
    sortingList() {
      return ['country', 'language', 'source']
    },
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
    clippingArray() {
      let clipping = []

      for (let el of this.clippingElements) {
        clipping.push({project: this.currentProject.id, post: el})
      }

      return clipping
    },
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    updatePostsCount(val) {
      this.countPosts = val
      this.isOpenDropdown = !this.isOpenDropdown
      this.$emit('update-posts-count', this.page, this.countPosts)
    },
    pageChangeHandler() {
      this.$emit('update-page', this.page, this.countPosts)
    },
    openDropdown() {
      this.isOpenDropdown = !this.isOpenDropdown
    },
    ...mapActions([
      action.REFRESH_DISPLAY_CALENDAR,
      action.DELETE_CLIPPING_FEED_CONTENT,
      action.CREATE_CLIPPING_FEED_CONTENT_WIDGET,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
    formatDate(date) {
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    openCalendar() {
      if (this.isShowCalendarContents) {
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
    openClippingDropdown() {
      this.isOpenClippingDropdown = !this.isOpenClippingDropdown
    },
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.clippingElements.push(id)
      } else {
        let element = this.clippingElements.indexOf(id)
        this.removeSelectedFilter(element, id)
      }
    },
    async removeSelectedFilter(index, id) {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.currentProject.id,
        postId: id,
      })
      this.clippingElements.splice(index, 1)
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](this.currentProject.id)
    },
    async createClippingWidget() {
      await this[action.CREATE_CLIPPING_FEED_CONTENT_WIDGET](this.clippingArray)
      await this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](
        this.currentProject.id
      )
    },
    selectedClippingElement(id) {
      return this.clippingContent.some((el) => el.post__id === id)
    },
    cardImg(item) {
      let images = [
        item.entry_media_content_url,
        item.entry_media_thumbnail_url,
        item.feed_image_href,
        item.feed_image_link,
      ]
      return images.filter((el) => el !== 'None')[0] || 'None'
    },
    selectItem(name, val) {
      this.$emit('add-sorting-value', val)
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

.pagination-wrapper {
  display: flex;
  justify-content: space-between;

  width: 100%;
  padding: 20px;
}

.clipping-wrapper {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;

  margin-left: 20px;

  .icon {
    cursor: pointer;

    color: var(--primary-text-color);
  }

  .icon-flip {
    transform: rotate(180deg);
  }

  .dropdown {
    z-index: 1000;

    position: absolute;
    top: 25px;
    left: -2px;

    display: flex;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--primary-text-color);

    .item {
      display: flex;
      gap: 10px;

      cursor: pointer;

      padding: 9px 16px 8px;

      &:hover {
        border-radius: 10px;
        background-color: var(--primary-button-color);
      }
    }
  }
}

.sorting-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  .sorting-select {
    width: 160px;
  }
}

.trigger-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  max-width: 100%;
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

.dropdown-wrapper {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;

  width: 61px;
  height: 34px;

  cursor: pointer;

  background: #242529;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 6px;

  .dropdown {
    z-index: 1000;

    position: absolute;
    top: 34px;
    right: 2px;

    display: flex;
    flex-direction: column;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--primary-text-color);

    .item {
      cursor: pointer;

      padding: 9px 24px 8px;

      &:hover {
        background-color: var(--primary-button-color);
      }
    }
  }
}

.filters {
  display: flex;
  align-items: center;
  gap: 20px;

  width: 100%;
  margin-bottom: 25px;

  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--secondary-text-color);
}

.search-results {
  margin-left: auto;
}

.arrow-open-dropdown {
  transform: rotate(180deg);
  color: var(--primary-button-color);
}

.arrow-down {
  cursor: pointer;

  width: 10px;
  height: 10px;

  margin: 0 0 0 7px;

  color: var(--primary-text-color);

  &:hover {
    color: var(--primary-button-color);
  }
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

<style lang="scss">
.pagination {
  display: flex;
  gap: 4px;

  .PaginationControl {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 34px;
    height: 34px;

    background: #242529;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 6px;

    color: var(--primary-text-color);

    .Control {
      fill: #333333;
    }

    .Control-active {
      fill: var(--primary-text-color);
    }
  }

  .Page {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 34px;
    height: 34px;

    background: #242529;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 6px;

    color: var(--primary-text-color);
  }
}
</style>
