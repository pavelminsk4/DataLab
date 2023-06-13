import PolicyView from '@/views/PolicyView'
import PrivacyScreen from '@components/policy/PrivacyScreen'
import TermsOfUseScreen from '@components/policy/TermsOfUseScreen'

export default [
  {
    name: 'Policy',
    path: '/policy',
    component: PolicyView,
    redirect: () => ({name: 'Privacy'}),
    children: [
      {
        name: 'Privacy',
        path: 'privacy',
        component: PrivacyScreen,
      },
      {
        name: 'Terms',
        path: 'terms-of-use',
        component: TermsOfUseScreen,
      },
    ],
  },
]
